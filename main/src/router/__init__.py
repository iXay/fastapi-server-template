"""
业务路由包

在这里按业务拆分子路由，例如：
- biz1 相关接口：`main.router.biz1`
- biz2 相关接口：`main.router.biz2`

使用方式：
    from main.router import biz1
    app.include_router(biz1.router)
"""
