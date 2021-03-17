import React, { Component } from 'react';
import { CanvasJSChart } from 'canvasjs-react-charts';
import './styles.css';

class Chart extends Component {
	constructor(props) {
		super(props);
		this.state = {
			text: "",
			filterData: [],
			links: [
			],
		}
	}
	fetchAPI = (url) => {
		let jsonBody = JSON.stringify({ url: url })
		fetch('http://localhost:8000/app/', {
			method: 'POST',
			body: jsonBody
		})
			.then((res) => res.json())
			.then(resultObj => {
				let data = resultObj;
				let url = data["url"];
				let result = data["result"];

				let topCateScores = this.getTopCategories(result, 5);
				let newspaper = {
					url: url,
					scores: topCateScores
				}
				let filterData = [...this.state.filterData, newspaper]
				this.setState({ filterData });
			})
	}

	getTopCategories(data, n) {
		var sortable = [];
		for (var cate in data) {
			sortable.push([cate, data[cate]]);
		}
		sortable.sort((a, b) => a[1] - b[1]);
		let filterData = sortable.slice(Object.keys(data).length - n);
		return filterData;
	}
	componentDidMount() {
	}

	getOptions(scores) {

		let dataPoints = scores.map(cateScore => {
			let label = cateScore[0]
			let scoreY = cateScore[1];
			return { label: label, y: scoreY}
		})
		const options = {
			animationEnabled: true,
			theme: "light2",
			title: {
				text: ""
			},
			axisX: {
				// title: "Chủ đề",
				reversed: true,
			},
			axisY: {
				includeZero: true,
				labelFormatter: this.addSymbols
			},
			data: [{
				type: "bar",
				dataPoints: dataPoints
			}]
		}
		console.log(options);
		return options;
	}

	handleChange = (event) => {
		this.setState({ text: event.target.value });
	}
	splitText2Urls = () => {
		let text = this.state.text;
		let links = text.split("\n");
		this.setState({links});
		return links;
	}

	handleSubmit = (event) => {
		this.setState({filterData: []})
		event.preventDefault();
		
		let links = this.splitText2Urls();
		links.forEach(link => {
			this.fetchAPI(link);
		})
	}
	render() {
		let { filterData } = this.state;
		console.log("render");
		console.log(filterData);
		return (
			<div>
				<form onSubmit={this.handleSubmit}>
					<label>
						<textarea rows="10" cols="50" value={this.state.value} onChange={this.handleChange} />
					</label>
					<input type="submit" value="Submit" />
				</form>
	
				<a href="https://github.com/nguyenvandai61/Topic_classification/blob/master/NewsExamples.txt">
				<label>NewsExamples.txt</label>
				</a>
				<div className="grid-container">
					{filterData.map(fd => (
						<div>
							<a href={fd.url}>{fd.url}</a>
							
							<CanvasJSChart class="grid-item" options={this.getOptions(fd.scores)} />
						</div>
					))}
				</div>
			</div>
		);
	}
}

export default Chart;