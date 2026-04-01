# common/middleware.py

class WitcherAuditMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            print(f"[CODEX LOG] Hunter '{request.user.username}' is accessing: {request.path}")
        else:
            print(f"[CODEX LOG] Guest is accessing: {request.path}")

        response = self.get_response(request)

        response['X-Codex-Version'] = '1.0-Witcher-Edition'

        return response