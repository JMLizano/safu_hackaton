function drawgraph(_nodes, _edges, containerElement) {
  // create an array with nodes 
  var nodes = new vis.DataSet(_nodes)

  // create an array with edges
  var edges = new vis.DataSet(_edges);

  // create a network
  var container = document.getElementById(containerElement);
  var data = {
    nodes: nodes,
    edges: edges
  };
  var options = {
    nodes: {borderWidth: 2},
    interaction: {hover: true},
    height: '600px',
    width: '100%'
  }
  var network = new vis.Network(container, data, options);

  // Allow to query for a node by clicking on it
  network.on( 'click', function(properties) {
    var ids = properties.nodes;
    var clickedNodes = nodes.get(ids);
    console.log('clicked nodes:', clickedNodes[0].label);
    $.ajax({
      url: "/",
      type: "post",
      data: {address: clickedNodes[0].label },
      success: function(response) {
        $("body").html(response);
      }
    });
  });
}