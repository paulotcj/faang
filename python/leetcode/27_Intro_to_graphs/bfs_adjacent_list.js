//-------------------------------------------------------------------------
const traversalBFS = function(graph) {
  const queue = [0];
  const values = [];
  const seen = {};

  //---------------------------
  while (queue.length) {
    const vertex = queue.shift();
    values.push(vertex);
    seen[vertex] = true;
    
    //---------------------------
    const connections = graph[vertex];
    for (let i = 0; i < connections.length; i++) {
      const connection = connections[i];
      if (!seen[connection]) {
        queue.push(connection);
      }
    }
    //---------------------------
  }
  //---------------------------

  return values;
}
//-------------------------------------------------------------------------

const adjacencyList = [
  [1, 3],         // 0
  [0],            // 1
  [3, 8],         // 2  
  [0, 2, 4, 5],   // 3
  [3, 6],         // 4
  [3],            // 5
  [4, 7],         // 6
  [6],            // 7
  [2]             // 8
];

const values = traversalBFS(adjacencyList)

console.log(values);

// (9) [0, 1, 3, 2, 4, 5, 8, 6, 7]

