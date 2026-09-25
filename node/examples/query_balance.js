const { QuantumTokenClient } = require("../index.js");

const API_KEY = process.env.QUANTOKEN_API_KEY || "YOUR_KEY_HERE";
const client = new QuantumTokenClient(API_KEY);

(async () => {
  console.log("=== balance ===");
  console.log(await client.balance());
})();
