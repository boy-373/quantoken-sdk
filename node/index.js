const fetch = require("node-fetch");

class QuantumTokenClient {
  constructor(apiKey, baseUrl = "https://trade.pianam.cn") {
    if (!apiKey) throw new Error("apiKey is required");
    this.apiKey = apiKey;
    this.baseUrl = baseUrl.replace(/\/$/, "");
  }

  async _request(path, options = {}) {
    const url = `${this.baseUrl}${path}`;
    const res = await fetch(url, {
      ...options,
      headers: {
        "X-API-Key": this.apiKey,
        "Content-Type": "application/json",
        "Accept": "application/json",
        ...options.headers,
      },
    });
    const body = await res.json().catch(() => null);
    if (!res.ok) throw new Error(JSON.stringify({ status: res.status, body }));
    return body;
  }

  async balance() {
    return this._request("/api/v1/open/quota");
  }

  async consume(amount = 1, idempotencyKey) {
    const payload = { amount };
    if (idempotencyKey) payload.idempotency_key = idempotencyKey;
    return this._request("/api/v1/open/quota/consume", {
      method: "POST",
      body: JSON.stringify(payload),
    });
  }

  /**
   * POST /api/v1/open/chat/completions (OpenAI compatible).
   * Returns a standard OpenAI Chat Completion object.
   * Tiers (credits/call): qwen-flash=1, qwen-turbo=2, qwen-plus=5.
   */
  async chat(messages, {
    model = "qwen-flash",
    maxTokens = 512,
    temperature,
    topP,
    stop,
    requestId,
  } = {}) {
    const payload = { model, messages, max_tokens: maxTokens };
    if (temperature !== undefined) payload.temperature = temperature;
    if (topP !== undefined) payload.top_p = topP;
    if (stop !== undefined) payload.stop = stop;
    if (requestId !== undefined) payload.request_id = requestId;
    return this._request("/api/v1/open/chat/completions", {
      method: "POST",
      body: JSON.stringify(payload),
    });
  }

  async openapiSchema() {
    return this._request("/openapi.json");
  }
}

module.exports = { QuantumTokenClient };
