import express from 'express';
import redis from 'redis';
import { promisify } from 'util';

const app = express();
const client = redis.createClient();
const listProducts = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    stock: 4,
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    stock: 10,
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    stock: 2,
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    stock: 5,
  },
];
function getItemById(id) {
  return listProducts.find((product) => product.id === id);
}
async function reserveStockById(itemId, stock) {
  const setAsync = promisify(client.set).bind(client);
  await setAsync(`item.${itemId}`, stock);
}
async function getCurrentReservedStockById(itemId) {
  const getAsync = promisify(client.get).bind(client);
  const stock = await getAsync(`item.${itemId}`);
  return stock ? parseInt(stock, 10) : 0;
}
app.get('/list_products', (req, res) => {
  res.json(listProducts.map((product) => ({
    itemId: product.id,
    itemName: product.name,
    price: product.price,
    initialAvailableQuantity: product.stock,
  })));
});
app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const reservedStock = await getCurrentReservedStockById(itemId);
    res.json({
      itemId: product.id,
      itemName: product.name,
      price: product.price,
      initialAvailableQuantity: product.stock,
      currentQuantity: product.stock - reservedStock,
    });
  }
});
app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId, 10);
  const product = getItemById(itemId);

  if (!product) {
    res.json({ status: 'Product not found' });
  } else {
    const reservedStock = await getCurrentReservedStockById(itemId);
    const stockAvailable = product.stock - reservedStock;

    if (stockAvailable <= 0) {
      res.json({ status: 'Not enough stock available', itemId });
    } else {
      await reserveStockById(itemId, reservedStock + 1);
      res.json({ status: 'Reservation confirmed', itemId });
    }
  }
});
app.listen(1245, () => {
  console.log('...');
});
