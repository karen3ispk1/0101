from src.server.routers import record, service, review, history, user, staff

routers = (
    record.router,
    service.router,
    review.router,
    history.router,
    user.router,
    staff.router,
    )
