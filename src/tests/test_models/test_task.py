from sqlalchemy.ext.asyncio import AsyncSession

from models import Task


class TestTaskModel:
    async def test_fields(self, async_session: AsyncSession) -> None:
        concurrent_fields_name = [i.name for i in Task.__table__.columns]
        related_fields = [
            i._dependency_processor.key for i in Task.__mapper__.relationships
        ]
        all_model_fields = concurrent_fields_name + related_fields
        schema_fields_name = {
            "name",
            "created_at",
            "description",
            "status",
        }
        for field in schema_fields_name:
            assert field in all_model_fields, (
                "Нет необходимого поля %s" % field
            )
