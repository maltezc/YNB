import React from 'react';
import ReactDOM from 'react-dom';
import 'bootstrap/dist/css/bootstrap.css'
import {
    Row, Col, CardBody, CardTitle, CardText
} from 'reactstrap';
import './index.css'

class YNB extends React.Component {
    constructor() {
        super(); //Whenever constructor is called, you must also call super like so.

        this.state = {
            'items': []
        }
    }
    componentDidMount() {
        this.getItems();

    }

    getItems() {
        fetch('http://127.0.0.1:8000/books/api/books/')
            .then(results => results.json())
            .then(results => this.setState({'items': results}));
    }
    render() {
        return (
            <ul>
                {this.state.items.map(function (item, index) {
                    return (
                        <ContentItem item={item} />

                    )
                }
                )}
            </ul>
        );
    }
}


class ContentItem extends React.Component {
        render() {
            return (
                <Row className="ContentItem" key={item.index}>
                    <Col xs="6">
                        <CardBody>
                            <CardTitle>
                                {this.props.item.title}
                            </CardTitle>
                            <CardText>
                                {this.props.item.content}
                            </CardText>
                        </CardBody>
                    </Col>
                </Row>
            )
        }
    }


ReactDOM.render(
    <YNB />,
    document.getElementById('root')
)