1.RFC3986
-  reserved    = gen-delims / sub-delims

  gen-delims  = ":" / "/" / "?" / "#" / "[" / "]" / "@"

  sub-delims  = "!" / "$" / "&" / "'" / "(" / ")"
              / "*" / "+" / "," / ";" / "="
  远程调用：浏览器 url 保留字符,做参数值的时候服务器不会收到
