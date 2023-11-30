const { createClient } = require('redis');

const log = (arg) => console.log(arg);

const txt0 = 'Redis client not connected to the server';
const txt1 = 'Redis client connected to the server';

const channel = 'holberton school channel';

const client = createClient();

client.on('error', (err) => log(`${txt0}: ${err.message}`));
client.on('connext', () => log(txt1));

const publishMessage = (message, time) => {
  setTimeout(() => {
    log(`About to send ${message}`);
    client.publish(channel, message);
  }, time);
};

publishMessage("Holberton Student #1 starts course", 100);
publishMessage("Holberton Student #2 starts course", 200);
publishMessage("KILL_SERVER", 300);
publishMessage("Holberton Student #3 starts course", 400);
