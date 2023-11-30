const { createClient, print } = require('redis');
const { promisify } = require('util');

const log = (arg) => console.log(arg);

const txt0 = 'Redis client not connected to the server';
const txt1 = 'Redis client connected to the server';

const client = createClient();
const getValue = promisify(client.get).bind(client);

client.on('error', (err) => log(`${txt0}: ${err.message}`));
client.on('connect', () => log(txt1));

const setNewSchool = (schoolName, value) => {
  client.set(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
  const value = await getValue(schoolName);
  log(value);
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
