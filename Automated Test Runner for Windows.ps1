#Automated Test Runner for Windows
#This script installs dependencies and runs Pytest.

Write-Host "Installing project dependencies from requirements.txt..."
pip install -r requirements.txt

Write-Host "Running Pytest unit tests..."
pytest
#Check the exit code of the last executed command ($LastExitCode).

if ($LastExitCode -eq 0) {
Write-Host "All tests passed successfully!"
exit 0
} else {
Write-Host "Tests failed. Please check the output for details."
exit 1
}