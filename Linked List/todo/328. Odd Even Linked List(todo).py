app.get('/', (req, res) => {
  res.send({ hi: 'there' });
});
// 处理路由为根目录的GET请求
// =>function: 处理这个route的handler，一旦express app接到route为'/'，method为GET的请求，这个函数就会执行
// req: 传入代表请求的参数，携带有关请求的所有信息
// res: 返回响应的参数，通过res可以定制这个route的响应
// res.send 返回响应的内容，立即执行（返回）

作者：武器大师1024
链接：https://juejin.cn/post/6844903508982906887
来源：稀土掘金
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
