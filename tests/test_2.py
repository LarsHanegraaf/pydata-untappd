import pandas as pd

from refactor_2 import transform


def test_transform():
    df = pd.DataFrame(
        [
            ["Fruity Blend", "IPA - Fruity", "5% ABV", "4.5", "1,200 Ratings", "Blenddata"],
            ["Tropical IPA", "IPA", "6% ABV", "4.3", "1,400 Ratings", "Blenddata"]
        ],
        columns=["name", "style", "abv", "rating", "num_ratings", "brewery"],
    )
    transformed_df = transform(df)

    expected_df = pd.DataFrame(
        [
            [5.5, 4.4, 1300.0]
        ],
        index=pd.Index(["IPA"], name='style'),
        columns=["abv", 'rating', 'num_ratings']
    )

    pd.testing.assert_frame_equal(transformed_df, expected_df)

def test_transform_beer_type():
    df = pd.DataFrame(
        [
            ["Smoothie", "Non-alcoholic-IPA", "0.0% ABV", "3.5", "1,111 Ratings", "Blenddata"]
        ],
        columns=["name", "style", "abv", "rating", "num_ratings", "brewery"],
    )
    transformed_df = transform(df)

    expected_df = pd.DataFrame(
        [
            [0.0, 3.5, 1111.0]
        ],
        index=pd.Index(["Non-alcoholic"], name='style'),
        columns=["abv", 'rating', 'num_ratings']
    )

    pd.testing.assert_frame_equal(transformed_df, expected_df)