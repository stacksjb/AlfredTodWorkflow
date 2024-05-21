#!/bin/sh

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Homebrew is installed
echo "Checking if Homebrew is installed..."
if ! command_exists brew; then
    echo "⚠️ Homebrew is not installed."
    echo "🛠️ Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
else
    echo "✅  Homebrew is already installed."
fi

# Check if rustup-init is installed
echo "Checking if Rust/Cargo is installed..."
if ! command_exists rustup-init; then
    echo "⚠️ rustup-init is not installed."
    echo "🛠️  Installing rustup-init..."
    brew install rustup-init
else
    echo "✅  Rust is installed."
fi

# Initialize rustup (this only needs to be done once)
echo "Checking if Rust is initialized..."
if ! command_exists rustup; then
    echo "🛠️ Initializing rustup..."
    rustup-init -y
    source "$HOME"/.cargo/env
else
    echo "✅  Rustup is initialized."
fi

# Check if "tod" is installed
echo "Checking if \"Tod\" is installed..."
if ! command_exists tod; then
    echo "⚠️ \"Tod\" is not installed. "
    echo "🛠️ Installing \"Tod\"..."
    cargo install tod
else
    echo "✅  \"Tod\" is installed."
fi

# Run "tod config check-version" and if successful, run "t q -c Alfred 'Test Task'"
if command_exists brew && command_exists rustup && command_exists tod; then
    echo "✅  All required tools are installed. Running \"tod config check-version\"..."
    if tod config check-version; then
        echo "✅  Version check successful."
        echo "Submitting Test Task to your Inbox..."

        if tod task q -c "Alfred Test Task"; then
            echo "✅  Test Task created! Check your Todoist Inbox."
        else
            echo "❌  Task Creation failed. Resetting config"
            tod config reset
            echo "❌  Config deleted. Check your internet connectivity, API key, or run 'tod config reset' and run again."
        fi
    else
        echo "❌  Version check failed. Check connectivity and try again."
    fi
else
    echo "❌  One or more tools are not installed correctly. Retry, install manually, or open a bug report."
fi
