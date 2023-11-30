const createPushNotificationsJobs = (jobs, queue) => {
  if (!Array.isArray(jobs)) {
    throw new Error('Jobs is not an array');
  }

  const txt = 'Notification job';

  jobs.forEach((obj) => {
    const job = queue.create('push_notification_code_3', obj);
    job
      .on('complete', () => console.log(`${txt} ${job.id} completed`))
      .on('failed', (err) => console.log(`${txt} ${job.id} failed: ${err}`))
      .on('progress', (progress) => console.log(`${txt} ${job.id} ${progress}% complete`));
      job.save((err) => {
        if (!err) console.log(`${txt} created: ${job.id}`);
      });
    });
};

module.exports = createPushNotificationsJobs;
