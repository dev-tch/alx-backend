import { createQueue } from 'kue';

const queue = createQueue();
const jobData = {
  phoneNumber: '5869488948',
  message: 'Token to change Password',
};
const job = queue.create('push_notification_code', jobData)
  .save((err) => {
    if (!err) {
      console.log(`Notification job created: ${job.id}`);
    }
  });
job.on('complete', () => {
  console.log('Notification job completed');
})
  .on('failed', () => {
    console.log('Notification job failed');
  });
