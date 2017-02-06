DROP TABLE IF EXISTS video_game;
CREATE TABLE video_game (
  Name text,
  Platform text,
  Year_of_Release text,
  Genre text,
  Publisher text,
    NA_Sales real,
    EU_Sales real,
    JP_Sales real,
    Other_Sales real,
    Global_Sales real,
    Critic_Score real,
    Critic_Count real,
    User_Score text,
    User_Count real,
    Developer text,
    Rating text
);