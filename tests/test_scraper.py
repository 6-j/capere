from capere.scraper import scrape_usernames


def test_scrape_usernames_batch():
    test_usernames = ["likelynotauser123", "octocat", "anotherfakeuser123"]

    results = scrape_usernames(test_usernames)

    assert isinstance(results, dict), "Results should be a dictionary."

    for username in test_usernames:
        assert username in results, f"Username '{username}' not found in results."

        assert isinstance(results[username], bool), f"Result for '{username}' should be a boolean."

    assert results["likelynotauser123"] == True, "This username should be available."
    assert results["octocat"] == False, "The username 'octocat' should be taken."
