import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

function setHashObject(hashKey, objectValue) {
  for (const [key, value] of Object.entries(objectValue)) {
    client.hset(hashKey, key, value, redis.print);
  }
}
async function displayHashObject(hashKey) {
  const asyncGetAllHash = promisify(client.hgetall).bind(client);
  const reply = await asyncGetAllHash(hashKey);
  console.log(reply);
}
const objectValue = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '29',
  Cali: '40',
  Paris: '2',
};
setHashObject('HolbertonSchools', objectValue);
displayHashObject('HolbertonSchools');
