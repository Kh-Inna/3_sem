using System;

namespace LevenshteinDistanceCalculator{
    public class LevenshteinDistance{
        public int Calculate(string word_1, string word_2){
            if (string.IsNullOrEmpty(word_1)){
                return word_2?.Length ?? 0;
            }
            if (string.IsNullOrEmpty(word_2)){
                return word_1.Length;
            }

            int Length_1 = word_1.Length;
            int Length_2 = word_2.Length;

            int[,] distanceMatrix = new int[Length_1 + 1, Length_2 + 1];

            for (int i = 0; i <= Length_1; i++){
                distanceMatrix[i, 0] = i;
            }
            for (int j = 0; j <= Length_2; j++){
                distanceMatrix[0, j] = j;
            }

            for (int i = 1; i <= Length_1; i++){
                for (int j = 1; j <= Length_2; j++){
                    int cost = (word_2[j - 1] == word_1[i - 1]) ? 0 : 1;

                    distanceMatrix[i, j] = Math.Min(
                        Math.Min(distanceMatrix[i - 1, j] + 1, distanceMatrix[i, j - 1] + 1),
                        distanceMatrix[i - 1, j - 1] + cost);
                }
            }
            return distanceMatrix[Length_1, Length_2];
        }

        public int Print(string word_1, string word_2, int MAX, int distance){
            if (distance < MAX){
                Console.WriteLine($"Дистанция между '{word_1}' и '{word_2}': {distance}");
            }
            return 0;
        }
    }

    class Program{
        static void Main(string[] args){
            int MAX = 2;

            LevenshteinDistance distanceCalculator = new LevenshteinDistance();

            string word_1 = "cat";
            string word_2 = "can";

            int distance = distanceCalculator.Calculate(word_1, word_2);

            distanceCalculator.Print(word_1, word_2, MAX, distance);

            word_2 = "sad";
            distance = distanceCalculator.Calculate(word_1, word_2);

            distanceCalculator.Print(word_1, word_2, MAX, distance);
        }
    }
}