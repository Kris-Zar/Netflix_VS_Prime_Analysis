import pandas as pd
import matplotlib.pyplot as plt


primeDf = pd.read_csv("Prime.csv")
netflixDf = pd.read_csv("Netflix.csv")


movies = [netflixDf[netflixDf["type"] == "Movie"], primeDf[primeDf["type"] == "Movie"]]
tvShows = [netflixDf[netflixDf["type"] == "TV Show"], primeDf[primeDf["type"] == "TV Show"]]

print("*" * 43, "Welcome to Netflix Vs Amazon Prime Content Analysis", "*" * 43)
print("For Following Analysis Enter Code:" )
print(
    "Code: Operations\n",
    "1. Show Content Distribution\n",
    "2. Show Content Details\n",
    "3. Show Rating Distribution\n",
    "4. Show Yearly Release Trends\n"
)

choice = int(input("Enter Code: "))

if choice == 1:
   
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    axs[0].pie([len(movies[0]), len(tvShows[0])], labels=["Movies", "TV Shows"], autopct="%1.1f%%")
    axs[1].pie([len(movies[1]), len(tvShows[1])], labels=["Movies", "TV Shows"], autopct="%1.1f%%")
    axs[0].set_title("Netflix Content Distribution")
    axs[1].set_title("Amazon Prime Content Distribution")
    plt.suptitle("Content Distribution: Netflix vs Amazon Prime")
    plt.tight_layout()
    plt.show()

elif choice == 2:
    print("\n--- Netflix Content Details ---")
    print(f"Total Titles: {len(netflixDf)}")
    print(f"Movies: {len(movies[0])}")
    print(f"TV Shows: {len(tvShows[0])}")
    print("\n--- Amazon Prime Content Details ---")
    print(f"Total Titles: {len(primeDf)}")
    print(f"Movies: {len(movies[1])}")
    print(f"TV Shows: {len(tvShows[1])}")

elif choice == 3:
    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    netflixDf["rating"].value_counts().head(10).plot(kind="bar", ax=axs[0], color="red")
    primeDf["rating"].value_counts().head(10).plot(kind="bar", ax=axs[1], color="blue")
    axs[0].set_title("Netflix Rating Distribution")
    axs[1].set_title("Amazon Prime Rating Distribution")
    plt.suptitle("Rating Distribution: Netflix vs Amazon Prime")
    plt.tight_layout()
    plt.show()

elif choice == 4:
    netflixDf["release_year"].value_counts().sort_index().tail(20).plot(label="Netflix", color="red")
    primeDf["release_year"].value_counts().sort_index().tail(20).plot(label="Amazon Prime", color="blue")
    plt.title("Yearly Release Trends: Netflix vs Amazon Prime")
    plt.xlabel("Year")
    plt.ylabel("Number of Titles")
    plt.legend()
    plt.tight_layout()
    plt.show()

else:
    print("Invalid Code! Please enter 1, 2, 3, or 4.")
