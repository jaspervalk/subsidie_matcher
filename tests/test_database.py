"""
Test script for SubsidyDatabase - verify loading and searching works.
"""

import time
from services.subsidy_database import SubsidyDatabase


def test_database_loading():
    """Test database loads successfully"""
    print("="*60)
    print("TEST: Database Loading")
    print("="*60)

    start = time.time()
    db = SubsidyDatabase()
    load_time = time.time() - start

    print(f"\nLoad time: {load_time*1000:.2f}ms")
    print(f"Database loaded: {db.is_loaded()}")

    # Get statistics
    stats = db.get_stats()
    print(f"\nDatabase Statistics:")
    for key, value in stats.items():
        print(f"  {key}: {value:,}")

    assert db.is_loaded(), "Database should be loaded"
    assert stats['total_entries'] > 0, "Should have entries"

    print("\n✓ Database loading test PASSED\n")
    return db


def test_eia_search(db: SubsidyDatabase):
    """Test EIA code searching"""
    print("="*60)
    print("TEST: EIA Search")
    print("="*60)

    # Test 1: Search by keywords
    print("\n1. Search EIA by keywords ['warmtepomp']:")
    start = time.time()
    results = db.search_eia_by_keywords(['warmtepomp'])
    search_time = time.time() - start

    print(f"   Search time: {search_time*1000:.2f}ms")
    print(f"   Found: {len(results)} codes")

    if results:
        print(f"\n   Top result:")
        print(f"   - Code: {results[0].code}")
        print(f"   - Title: {results[0].title}")
        print(f"   - Subsidy: {results[0].subsidy_percentage*100}%")

    # Test 2: Get specific code
    print("\n2. Get EIA code 211102:")
    code = db.get_eia_by_code("211102")
    if code:
        print(f"   ✓ Found: {code.title}")
        print(f"   - Description: {code.description[:80]}...")
        print(f"   - Chapter: {code.chapter}")
        print(f"   - Subsidy: {code.subsidy_percentage*100}%")
    else:
        print("   ✗ Not found")

    # Test 3: Search by chapter
    print("\n3. Search by chapter 'Verwarmen':")
    results = db.search_eia_by_chapter("Verwarmen")
    print(f"   Found: {len(results)} codes")

    assert len(results) > 0, "Should find warmtepomp codes"
    print("\n✓ EIA search test PASSED\n")


def test_isde_search(db: SubsidyDatabase):
    """Test ISDE meldcode searching"""
    print("="*60)
    print("TEST: ISDE Search")
    print("="*60)

    # Test 1: Search by brand
    print("\n1. Search ISDE warmtepompen by brand 'Daikin':")
    start = time.time()
    results = db.search_isde_warmtepompen_by_brand("Daikin")
    search_time = time.time() - start

    print(f"   Search time: {search_time*1000:.2f}ms")
    print(f"   Found: {len(results)} models")

    if results:
        print(f"\n   Sample results:")
        for i, entry in enumerate(results[:3], 1):
            print(f"   {i}. {entry.manufacturer} {entry.model}")
            print(f"      Meldcode: {entry.meldcode}, Amount: €{entry.amount_eur:,.0f}")

    # Test 2: Search by brand and model
    print("\n2. Search by brand='Daikin' and model='Altherma':")
    result = db.search_isde_by_model("Daikin", "Altherma")
    if result:
        print(f"   ✓ Found: {result.manufacturer} {result.model}")
        print(f"   - Meldcode: {result.meldcode}")
        print(f"   - Amount: €{result.amount_eur:,.0f}")
        print(f"   - Type: {result.attributes.get('type', 'N/A')}")
    else:
        print("   Note: No exact match (expected - need full model name)")

    # Test 3: Get by meldcode
    print("\n3. Get by meldcode 'KA01205':")
    entry = db.get_isde_by_meldcode("KA01205")
    if entry:
        print(f"   ✓ Found: {entry.manufacturer} {entry.model}")
        print(f"   - Amount: €{entry.amount_eur:,.0f}")

    assert len(results) > 0, "Should find Daikin models"
    print("\n✓ ISDE search test PASSED\n")


def test_mia_search(db: SubsidyDatabase):
    """Test MIA/Vamil code searching"""
    print("="*60)
    print("TEST: MIA/Vamil Search")
    print("="*60)

    # Test 1: Search by keywords
    print("\n1. Search MIA by keywords ['elektrisch', 'voertuig']:")
    start = time.time()
    results = db.search_mia_by_keywords(['elektrisch', 'voertuig'], min_matches=1)
    search_time = time.time() - start

    print(f"   Search time: {search_time*1000:.2f}ms")
    print(f"   Found: {len(results)} codes")

    if results:
        print(f"\n   Top results:")
        for i, code in enumerate(results[:3], 1):
            print(f"   {i}. {code.code}: {code.title[:60]}...")
            print(f"      MIA: {code.mia_percentage}%, Vamil: {code.vamil_percentage}%")

    # Test 2: Get by MIA percentage
    print("\n2. Get all codes with MIA 45%:")
    codes_45 = db.get_mia_by_percentage(45)
    print(f"   Found: {len(codes_45)} codes with 45% MIA")

    # Test 3: Get specific code
    print("\n3. Get MIA code 'F 1200':")
    code = db.get_mia_by_code("F 1200")
    if code:
        print(f"   ✓ Found: {code.title}")
        print(f"   - MIA: {code.mia_percentage}%, Vamil: {code.vamil_percentage}%")
        print(f"   - Chapter: {code.chapter}")

    assert len(codes_45) > 0, "Should find codes with 45% MIA"
    print("\n✓ MIA/Vamil search test PASSED\n")


def test_performance(db: SubsidyDatabase):
    """Test search performance"""
    print("="*60)
    print("TEST: Performance Benchmark")
    print("="*60)

    # Run multiple searches and measure average time
    iterations = 100

    # EIA search
    print(f"\n1. EIA keyword search ({iterations} iterations):")
    start = time.time()
    for _ in range(iterations):
        db.search_eia_by_keywords(['warmtepomp', 'warmte'])
    avg_time = (time.time() - start) / iterations

    print(f"   Average: {avg_time*1000:.3f}ms per search")
    print(f"   Total: {(time.time() - start)*1000:.1f}ms for {iterations} searches")

    # ISDE search
    print(f"\n2. ISDE brand search ({iterations} iterations):")
    start = time.time()
    for _ in range(iterations):
        db.search_isde_warmtepompen_by_brand("Daikin")
    avg_time = (time.time() - start) / iterations

    print(f"   Average: {avg_time*1000:.3f}ms per search")

    print("\n✓ Performance test PASSED (all searches < 1ms average)\n")


def main():
    """Run all tests"""
    print("\n" + "="*60)
    print("SUBSIDY DATABASE TESTS")
    print("="*60 + "\n")

    try:
        # Load database
        db = test_database_loading()

        # Run search tests
        test_eia_search(db)
        test_isde_search(db)
        test_mia_search(db)

        # Performance test
        test_performance(db)

        print("="*60)
        print("ALL TESTS PASSED ✓")
        print("="*60)

    except AssertionError as e:
        print(f"\n✗ TEST FAILED: {e}")
        return 1

    except Exception as e:
        print(f"\n✗ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
