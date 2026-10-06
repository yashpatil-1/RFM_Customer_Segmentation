import subprocess
import sys


SCRIPTS = [
    "src/data_inspection.py",
    "src/data_quality.py",
    "src/data_cleaning.py",
    "src/rfm_analysis.py",
    "src/rfm_scoring.py",
    "src/customer_segmentation.py",
    "src/visualizations.py",
    "src/business_insights.py",
]


def run_script(script):
    print("\n" + "=" * 70)
    print(f"RUNNING: {script}")
    print("=" * 70)

    result = subprocess.run(
        [sys.executable, script],
        check=False
    )

    if result.returncode != 0:
        print(f"\nERROR: {script} failed.")
        sys.exit(result.returncode)


def main():
    print("=" * 70)
    print("RFM CUSTOMER SEGMENTATION PIPELINE")
    print("=" * 70)

    for script in SCRIPTS:
        run_script(script)

    print("\n" + "=" * 70)
    print("FULL PIPELINE COMPLETED SUCCESSFULLY")
    print("=" * 70)

    print("\nGenerated outputs:")
    print("✓ Clean transaction dataset")
    print("✓ RFM analysis")
    print("✓ RFM scoring")
    print("✓ Customer segmentation")
    print("✓ Visualization suite")
    print("✓ Business insights")


if __name__ == "__main__":
    main()