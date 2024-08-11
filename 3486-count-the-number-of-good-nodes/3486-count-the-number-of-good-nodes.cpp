class Solution {
public:
    int countGoodNodes(vector<vector<int>>& edges) {
        int n = edges.size() + 1;
        vector<vector<int>> adjacencyList(n);
        for (auto& edge : edges) {
            adjacencyList[edge[0]].push_back(edge[1]);
            adjacencyList[edge[1]].push_back(edge[0]);
        }
        
        vector<int> subtreeSizes(n, 0);
        int goodNodesCount = 0;
        computeSubtreeSizes(adjacencyList, subtreeSizes, goodNodesCount, 0, -1);
        
        return goodNodesCount;
    }
    
private:
    int computeSubtreeSizes(vector<vector<int>>& adjacencyList, vector<int>& subtreeSizes, int& goodNodesCount, int currentNode, int parentNode) {
        int currentSize = 1;
        unordered_map<int, int> sizeFrequency;
        
        for (int neighbor : adjacencyList[currentNode]) {
            if (neighbor == parentNode) continue;
            int childSubtreeSize = computeSubtreeSizes(adjacencyList, subtreeSizes, goodNodesCount, neighbor, currentNode);
            currentSize += childSubtreeSize;
            sizeFrequency[childSubtreeSize]++;
        }
        
        if (sizeFrequency.size() <= 1) goodNodesCount++;
        subtreeSizes[currentNode] = currentSize;
        return currentSize;
    }

    void buildGraph(const vector<vector<int>>& edges, vector<vector<int>>& adjacencyList) {
        int n = edges.size() + 1;
        adjacencyList.resize(n);
        for (const auto& edge : edges) {
            adjacencyList[edge[0]].push_back(edge[1]);
            adjacencyList[edge[1]].push_back(edge[0]);
        }
    }
};