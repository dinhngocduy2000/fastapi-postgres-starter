from typing import Optional, List
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.user import User
from app.schemas.user import UserCreate, UserUpdate
from app.core.security import get_password_hash, verify_password


class UserCRUD:
    """CRUD operations for User model"""
    
    async def get(self, db: AsyncSession, user_id: int) -> Optional[User]:
        """Get a user by ID"""
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()
    
    async def get_by_email(self, db: AsyncSession, email: str) -> Optional[User]:
        """Get a user by email"""
        result = await db.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()
    
    async def get_by_username(self, db: AsyncSession, username: str) -> Optional[User]:
        """Get a user by username"""
        result = await db.execute(select(User).where(User.username == username))
        return result.scalar_one_or_none()
    
    async def get_multi(self, db: AsyncSession, skip: int = 0, limit: int = 100) -> List[User]:
        """Get multiple users"""
        result = await db.execute(select(User).offset(skip).limit(limit))
        return result.scalars().all()
    
    async def create(self, db: AsyncSession, user_in: UserCreate) -> User:
        """Create a new user"""
        db_user = User(
            email=user_in.email,
            username=user_in.username,
            hashed_password=get_password_hash(user_in.password),
            full_name=user_in.full_name
        )
        db.add(db_user)
        await db.flush()
        await db.refresh(db_user)
        return db_user
    
    async def update(self, db: AsyncSession, user: User, user_in: UserUpdate) -> User:
        """Update a user"""
        update_data = user_in.model_dump(exclude_unset=True)
        
        if "password" in update_data:
            hashed_password = get_password_hash(update_data["password"])
            del update_data["password"]
            update_data["hashed_password"] = hashed_password
        
        for field, value in update_data.items():
            setattr(user, field, value)
        
        await db.flush()
        await db.refresh(user)
        return user
    
    async def delete(self, db: AsyncSession, user_id: int) -> Optional[User]:
        """Delete a user"""
        user = await self.get(db, user_id)
        if user:
            await db.delete(user)
            await db.flush()
        return user
    
    async def authenticate(self, db: AsyncSession, username: str, password: str) -> Optional[User]:
        """Authenticate a user"""
        user = await self.get_by_username(db, username)
        if not user:
            return None
        if not verify_password(password, user.hashed_password):
            return None
        return user


user_crud = UserCRUD()

