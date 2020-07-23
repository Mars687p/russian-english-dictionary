from tortoise import Tortoise

db_url='sqlite://db.sqlite3'

async def init():
    await Tortoise.init(
        db_url=db_url,
        modules={'models': ['app.models']}
    )
    await Tortoise.generate_schemas()