WITH base AS (
    SELECT
        CAST(viewCount AS INTEGER) AS views,
        CAST(likeCount AS INTEGER) AS likes
    FROM {{ ref('processed_data') }}
)

SELECT
    views,
    likes,
    likes / views AS like_ratio
FROM base
