from aiohttp import web

from route import APIHaveRoute, HTTPHaveRoute

api_route = APIHaveRoute()
http_route = HTTPHaveRoute()
router = web.RouteTableDef()


