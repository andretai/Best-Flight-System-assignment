var graph = [
    'AB6',
    'AC3',
    'BD6',
    'CD5',
    'CE9',
    'DF8',
    'DE3',
    'EG8',
    'FG2'
  ];
  
  var parseEdge = (edge) => {
    var [left, right, ...cost] = edge;
    cost = parseInt(cost.join(''), 10);
    return { left, right, cost };
  };
  
  var addToMap = (map, origin, vertex, cost) => {
    (map[origin] = map[origin] || [])
      .push({ vertex, cost });
  };
  
  var graphToMap = (graph) => {
    var map = {};
  
    for (var edge of graph) {
      var { left, right, cost } = parseEdge(edge);
  
      addToMap(map, left, right, cost);
      addToMap(map, right, left, cost);
    }
  
    return map;
  };
  
  var tableToString = (table) => {
    return Object.keys(table)
      .map(vertex => {
        var { vertex: from, cost } = table[vertex];
        return `${vertex}: ${cost} via ${from}`;
      })
      .join('\n');
  };
  
  var tracePath = (table, start, end) => {
    var path = [];
    var next = end;
    while (true) {
      path.unshift(next);
      if (next === start) { break; }
      next = table[next].vertex;
    }
  
    return path;
  };
  
  var run = (graph, start, end) => {
    var map = graphToMap(graph);
  
    // console.log(map);
  
    var visited = [];
    var frontier = [start];
    var table = { [start]: { vertex: start, cost: 0 } };
  
    var vertex;
    while (vertex = frontier.shift()) {
      // Explore unvisited neighbors
      var neighbors = map[vertex]
        .filter(n => !visited.includes(n.vertex));
  
      // Add neighbors to the frontier
      frontier.push(...neighbors.map(n => n.vertex));
  
      var costToVertex = table[vertex].cost;
  
      for (let { vertex: to, cost } of neighbors) {
        var currCostToNeighbor = table[to] && table[to].cost;
        var newCostToNeighbor = costToVertex + cost;
        if (currCostToNeighbor == undefined ||
            newCostToNeighbor < currCostToNeighbor) {
          // Update the table
          table[to] = { vertex, cost: newCostToNeighbor };
        }
      }
  
      visited.push(vertex);
    }
  
    // console.log(table);
  
    console.log('Here you go:');
    console.log(tableToString(table));
  
    var path = tracePath(table, start, end);
  
    console.log('');
    console.log('Shortest path is:');
    console.log(path.join('->'));
  };
  
  run(graph, 'A', 'G');