import builtwith

def detect_tech(url):
    print("\n[TECHNOLOGIES DETECTED]")
    try:
        tech = builtwith.parse(url)
        for key, value in tech.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(f"Tech detection failed: {e}")
