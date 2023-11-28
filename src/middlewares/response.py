from fastapi import Request, Response

from src.utils.logger import ResponseLogContent, res_logger


async def response_handler(req: Request, call_next: callable):
    res: Response = await call_next(req)
    res_content = ResponseLogContent(
        path=req.url.path,
        method=req.method,
        ip_address=req.client.host,
        status_code=res.status_code,
    )
    res_logger.info(str(res_content.model_dump()))
    return res
