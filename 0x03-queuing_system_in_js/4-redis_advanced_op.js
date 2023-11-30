const { createClient, print } = require('redis');

const log = (arg) => console.log(arg);

const txt0 = 'Redis client not connected to the server';
const txt1 = 'Redis client connected to the server';

const HASHKEY = 'HolbertonSchools';

const obj = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
}

const client = createClient();

client.on('error', (err) => log(`${txt0}: ${err.message}`));
client.on('connext', () => log(txt1));

Object.entries(obj).forEach(([key, value]) => {
  client.hset(HASHKEY, key, value, print);
});

client.hgetall(HASHKEY, (err, hash) => {
  if (err) {
    throw err;
  }

  log(hash);
});
