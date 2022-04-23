import uvicorn 


def main():
    """
    Main for runs a fastapi server
    """
    uvicorn.run(
        "config.app:application",
        host="0.0.0.0",
        port=8000,
        reload=True,
    )


if __name__ == "__main__":
    main()