const kue = require('kue');

const log = (arg) => console.log(arg);

const queue = kue.createQueue();
const obj = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
}

const job = queue.create('push_notification_code', obj).save();

job.on('enqueue', () => log(`Notification job created: ${job.id}`))
  .on('complete', () => log('Notification job completed'))
  .on('failed', () => log('Notification job failed'));
