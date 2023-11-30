const { createClient } = require('redis');

const log = (arg) => console.log(arg);

const txt0 = 'Redis client not connected to the server';
const txt1 = 'Redis client connected to the server';

const client = createClient();

client.on('error', (err) => log(`${txt0}: ${err.message}`));
client.on('connext', () => log(txt1));

client.subscribe('holberton school channel');

client.on('message', (err, message) => {
  log(message);

  if (message == 'KILL_SERVER') {
    client.unsubscribe();
    client.quit();
  }
});
