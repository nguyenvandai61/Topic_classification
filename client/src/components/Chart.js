import React, { Component } from 'react';
import { CanvasJSChart } from 'canvasjs-react-charts';
import './styles.css';

class Chart extends Component {
	constructor(props) {
		super(props);
		this.state = {
			filterData: [],
			links: [
				'https://vnexpress.net/doi-the-bao-hiem-y-te-moi-khong-phat-sinh-chi-phi-4249450.html', 
				'https://vnexpress.net/trump-lenh-denh-hau-nha-trang-4248434.html',
				'https://vnexpress.net/giai-ma-ac-mong-chan-thuong-o-real-4249124.html',
				'https://vnexpress.net/chang-tho-moc-keo-xe-tai-1-5-tan-di-bo-42-km-4249160.html',
				'https://vnexpress.net/phap-dieu-tra-bien-chung-ncov-nghi-ne-xet-nghiem-4249491.html'
			
		],
		}
	}
	fetchAPI = (url) => {
		let jsonBody = JSON.stringify({url: url})
		fetch('http://localhost:8000/app/', {
			method: 'POST',
			body: jsonBody
		})
			.then((res) => res.json())
			.then(resultObj => {
				let data = resultObj;
				let result = data["result"];
				let newVal = this.getTopCategories(result, 5);
				console.log(newVal);
				let filterData = [...this.state.filterData, newVal] 
				this.setState({filterData});
			})
	}

	getTopCategories(data, n) {
		var sortable = [];
		for (var cate in data) {
			sortable.push([cate, data[cate]]);
		}
		sortable.sort((a, b) => a[1]-b[1]);
		let filterData = sortable.slice(Object.keys(data).length - n);
		console.log(filterData);
		return filterData;
	}
	componentDidMount() {
		this.state.links.forEach(link => {
			this.fetchAPI(link);
		})
	}

	getOptions(filterData) {
		console.log(filterData)
		let dataPoints = filterData.map(d => {
			return {y: d[1], label: d[0]}
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
	render() {
		let {filterData} = this.state;
		return (
			<div className="grid-container">
				{filterData.map(fd => (
					<CanvasJSChart class="grid-item" options={this.getOptions(fd)} />
				))}
			</div>
		);
	}
}

export default Chart;