from sqlalchemy.ext.asyncio import AsyncConnection
from sqlalchemy.sql import select

from ...models.raw import mstCommandCode


async def get_cc_id(conn: AsyncConnection, col_no: int) -> int:
    stmt = select(mstCommandCode.c.id).where(mstCommandCode.c.collectionNo == col_no)
    mstCc_db = (await conn.execute(stmt)).fetchone()
    if mstCc_db:
        return int(mstCc_db.id)
    return col_no