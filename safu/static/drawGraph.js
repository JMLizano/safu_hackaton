function drawgraph(s, origin, outgoing, incoming) {
  
  s.graph.clear();

  s.graph.addNode({
    // Main attributes:
    id: origin.id,
    label: origin.id,
    // Display attributes:
    x: Math.random(),
    y: Math.random(),
    size: 1,
    color: origin.compromised ? '#ff0000': '#0000ff'
  });

  for(index in outgoing) {
    address = outgoing[index]
    s.graph.addNode({
      // Main attributes:
      id: address.id,
      label: address.id,
      // Display attributes:
      x: Math.random(),
      y: Math.random(),
      size: 1,
      color: address.compromised ? '#ff0000': '#0000ff'
    });

    s.graph.addEdge({
      id: "out_" + address.id,
      source: origin.id,
      target: address.id,
      color: '#000000',
      type: 'arrow'
    });
  }

  for(index in incoming) {
    address = incoming[index]
    if (!s.graph.nodes(address.id)) {
      s.graph.addNode({
        // Main attributes:
        id: address.id,
        label: address.id,
        // Display attributes:
        x: Math.random(),
        y: Math.random(),
        size: 1,
        color: address.compromised ? '#ff0000': '#0000ff'
      });
    }

    s.graph.addEdge({
      id: "in_" + address.id,
      source: address.id,
      target: origin.id,
      color: '#000000',
      type: 'arrow'
    });
  }

  sigma.plugins.relativeSize(s, 1);
  s.refresh();
  s.startForceAtlas2();
  window.setTimeout(function() {s.killForceAtlas2()}, 250);
}

function metrics(node) {
  $('#outgoing').css('width', node.outgoing_transactions.length+'%').attr('aria-valuenow', node.outgoing_transactions.length);
  $('#incoming').css('width', node.incoming_transactions.length+'%').attr('aria-valuenow', node.incoming_transactions.length);
}