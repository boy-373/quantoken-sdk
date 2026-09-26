// AI chat example (OpenAI compatible). Docs: https://trade.pianam.cn/docs
// Run: node examples/chat.js
const { QuantokenClient } = require("../index.js");

const client = new QuantokenClient("YOUR_API_KEY");

(async () => {
  const resp = await client.chat(
    [{ role: "user", content: "用一句话解释什么是向量数据库" }],
    {
      model: "qwen-flash", // tiers: qwen-flash=1, qwen-turbo=2, qwen-plus=5 credits
      requestId: "demo-chat-001", // idempotent retries
    },
  );
  console.log(resp.choices[0].message.content);
  console.log("remaining credits:", resp.remaining);
})();
