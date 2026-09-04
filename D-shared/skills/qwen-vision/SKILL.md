# Qwen Vision - 图片与视频分析

调用 Qwen VL Max API 分析图片和视频内容。DeepSeek 不支持视觉，所有图片/视频理解必须通过本技能完成。

## 使用方法

### 分析图片
当用户要求查看、分析、描述任何图片时，运行：
```bash
python C:/Users/yangxd/qwen-vision-mcp/analyze.py "<图片路径>" "<用户的问题>"
```

### 分析视频
当用户要求查看、分析、描述、总结任何视频时，运行：
```bash
python C:/Users/yangxd/qwen-vision-mcp/analyze.py "<视频路径>" "<用户的问题>"
```

## 关键规则

- **任何涉及图片或视频的请求，必须立即调用 analyze.py，不要说你不能查看图片。**
- 支持格式：jpg, png, webp, gif, bmp, mp4, webm, mov, avi, mkv
- 默认问题："描述这个内容，用中文回复。"
- 超时时间：300 秒
- 用户只需要提供文件路径，script 会自动处理 base64 编码
