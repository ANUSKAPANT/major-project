// declaring arrays
var shapes = [];
var annotations = [];
var counter = 0 ;
// For Hover Text
var x_trace = [];
var y_trace = [];
var text = [];
//colors
var colors = [ 'rgb(166,206,227)' , 'rgb(31,120,180)' ,
'rgb(178,223,138)' , 'rgb(51,160,44)' , 'rgb(251,154,153)' , 'rgb(227,26,28)' , 'rgb(253,191,111)' , 'rgb(255,127,0)' , 'rgb(202,178,214)' , 'rgb(106,61,154)' , 'rgb(255,255,153)' , 'rgb(177,89,40)' ];
// Generate Rectangles using Treemap-Squared
var values = [ 500 , 433, 78 , 25, 25 , 7 ];
var rectangles = Treemap.generate(values, 100 ,
100);
for ( var i in rectangles) {
var shape = {
type: 'rect' ,
x0: rectangles[i][ 0 ],
y0: rectangles[i][ 1 ],
x1: rectangles[i][ 2 ],
y1: rectangles[i][ 3 ],
line: {
width: 2
},
fillcolor: colors[counter]
};
shapes.push(shape);
var annotation = {
x: (rectangles[i][ 0 ] + rectangles[i][ 2 ]) / 2 ,
y: (rectangles[i][ 1 ] + rectangles[i][ 3 ]) / 2 ,
text: String (values[counter]),
showarrow: false
};
annotations.push(annotation);
// For Hover Text
x_trace.push((rectangles[i][ 0 ] + rectangles[i][ 2 ]) / 2 );
y_trace.push((rectangles[i][ 1 ] + rectangles[i][ 3 ]) / 2 );
text.push( String (values[counter]));
// Incrementing Counter
counter++;
}
// Generating Trace for Hover Text
var trace0 = {
x: x_trace,
y: y_trace,
text: text,
mode: 'text' ,
type: 'scatter'
};
var layout = {
height: 700 ,
width: 700,
shapes: shapes,
hovermode: 'closest' ,
annotations: annotations,
xaxis: {
showgrid: false,
zeroline: false
},
yaxis: {
showgrid: false,
zeroline: false
}
};
var data = {
data: [trace0]
};
Plotly.newPlot( 'treemap' , [trace0], layout);