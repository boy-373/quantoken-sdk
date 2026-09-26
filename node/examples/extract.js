// Web extraction example. Docs: https://trade.pianam.cn/docs
// Run: node examples/extract.js
const { QuantokenClient } = require("../index.js");

const client = new QuantokenClient("YOUR_API_KEY");

(async () => {
  // structured fields from a URL
  const resp = await client.extract({
    url: "https://example.com",
    fields: { title: "page title", desc: "one-sentence summary" },
    request_id: "demo-extract-001",
  });
  console.log(resp.data);
  console.log("remaining credits:", resp.remaining);
})();
