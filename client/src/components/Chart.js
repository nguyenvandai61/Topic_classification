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
			message: ""
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
				if (result == null) {
					let newspaper = {
						url: url,
						message: "Failed in process!"
					}
						
					let filterData = [...this.state.filterData, newspaper]
					this.setState({ filterData });
					return;
				};

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
	validURL = (str) => {
		var pattern = new RegExp('^(https?:\\/\\/)?'+ // protocol
		  '((([a-z\\d]([a-z\\d-]*[a-z\\d])*)\\.)+[a-z]{2,}|'+ // domain name
		  '((\\d{1,3}\\.){3}\\d{1,3}))'+ // OR ip (v4) address
		  '(\\:\\d+)?(\\/[-a-z\\d%_.~+]*)*'+ // port and path
		  '(\\?[;&a-z\\d%_.~+=-]*)?'+ // query string
		  '(\\#[-a-z\\d_]*)?$','i'); // fragment locator
		return !!pattern.test(str);
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
		event.preventDefault();
		this.setState({filterData: [], links: []});
		
		let links = this.splitText2Urls();
		links.forEach(link => {
			if (this.validURL(link))
				this.fetchAPI(link);
			else {
				let newspaper = {
					url: link,
					message: "Invalid URL"
				}
					
				let filterData = [...this.state.filterData, newspaper]
				this.setState({ filterData });
			}
		})
	}
	render() {
		let { filterData } = this.state;
		return (
			<div>
				<form onSubmit={this.handleSubmit}>
					<label>
						<textarea rows="10" cols="100" value={this.state.value} onChange={this.handleChange} />
					</label>
					<input type="submit" value="Submit" />
				</form>
	
				<a href="https://github.com/nguyenvandai61/Topic_classification/blob/master/NewsExamples.txt">
				<label>NewsExamples.txt</label>
				</a>
				<div className="grid-container">
					{filterData.map((fd, idx) => (
						<div>
							<label>{idx+1}. </label>
							<a href={fd.url}>{fd.url}</a>
							{
							!!fd.scores? (
								<CanvasJSChart class="grid-item" options={this.getOptions(fd.scores)} />
							): (<div>
								{fd.message}
							</div>)
							}
						</div>
					))}
				</div>
			</div>
		);
	}
}

export default Chart;