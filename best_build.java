class Player {
  public int age;
  public int score;
  public Player(int age, int score) {
    this.age = age;
    this.score = score;
  }
};

class Solution {
  public int bestTeamScore(int[] scores, int[] ages) {
    final int n = scores.length;
    Player[] players = new Player[n];
    int[] dp = new int[n];

    for (int i = 0; i < n; ++i)
      players[i] = new Player(ages[i], scores[i]);

    Arrays.sort(players, (a, b) -> a.age == b.age ? b.score - a.score : b.age - a.age);

    for (int i = 0; i < n; ++i) {
      
      dp[i] = players[i].score;
      
      for (int j = 0; j < i; ++j)
        if (players[j].score >= players[i].score)
          dp[i] = Math.max(dp[i], dp[j] + players[i].score);
    }

    return Arrays.stream(dp).max().getAsInt()
  }
}
