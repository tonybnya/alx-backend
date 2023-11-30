const kue = require('kue')
const queue = kue.createQueue();

const numBlacklisted = [ 4153518780, 4153518781 ];
const log = (arg) => console.log(arg);

const sendNotification = (phoneNumber, message, job, done) => {
  job.progress(0, 100);

  if (numBlacklisted.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
  }

  job.progress(50, 100);
  log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();

  const queue = kue.createQueue();

  queue.process('push_notification_code_2', 2, (job, done) => {
    const { phoneNumber, message } = job.data;
    sendNotification(phoneNumber, message, job, done);
  });
};
