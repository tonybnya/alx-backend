const { createClient, print } = require('redis');

const log = (arg) => console.log(arg);

const txt0 = 'Redis client not connected to the server';
const txt1 = 'Redis client connected to the server';

const client = createClient();

client.on('error', (err) => log(`${txt0}: ${err.message}`));
client.on('connect', () => log(txt1));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = (schoolName) => {
  client.get(schoolName, (err, value) => {
    if (err) {
      throw err
    }
    log(value);
  });
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
