"""Quick test to verify the API endpoint works correctly."""
import asyncio
import json
from datetime import date, timedelta

from app.services.plan_service import PlanService
from app.schemas import PlanRequest


async def main():
    service = PlanService()
    
    print(f"🔧 Using provider: {service.provider_name()}")
    print("=" * 60)
    
    # Test request
    request = PlanRequest(
        goal="Launch a productivity app in 2 weeks",
        target_date=date.today() + timedelta(days=14),
        guidance="Team of 3 engineers, budget is tight, prioritize MVP",
    )
    
    print(f"📋 Goal: {request.goal}")
    print(f"🎯 Target: {request.target_date}")
    print(f"💡 Guidance: {request.guidance}")
    print("=" * 60)
    print("⏳ Generating plan...\n")
    
    try:
        response = await service.generate(request)
        
        print(f"✅ Plan generated successfully!")
        print(f"📊 Strategy: {response.metadata.planning_strategy}")
        print(f"⚙️  Tasks: {len(response.tasks)}")
        print("=" * 60)
        
        for i, task in enumerate(response.tasks, 1):
            print(f"\n{i}. {task.title}")
            print(f"   ID: {task.id}")
            if task.description:
                print(f"   Description: {task.description[:80]}...")
            if task.start_date and task.due_date:
                print(f"   Timeline: {task.start_date} → {task.due_date}")
            if task.depends_on:
                print(f"   Depends on: {', '.join(task.depends_on)}")
            if task.confidence:
                print(f"   Confidence: {task.confidence:.0%}")
        
        print("\n" + "=" * 60)
        print("✨ Test completed successfully!")
        
    except Exception as exc:
        print(f"❌ Error: {exc}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
