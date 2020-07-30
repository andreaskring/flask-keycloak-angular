import { Component, OnInit } from '@angular/core';
import { DataService } from '../services/data.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-public',
  templateUrl: './public.component.html',
  styleUrls: ['./public.component.css']
})
export class PublicComponent implements OnInit {


  obj: object = {foo: 'hurra'};

  objs: object[] = [
    {abc: 'xyz'}
  ];

  names: string[] = ['Bruce Lee', 'Bob Sacamento'];

  title = 'angular';

  myObserver = {
    next: obj => this.obj = obj,
    error: err => this.obj = {msg: 'error'},
    complete: () => console.log('Observer got complete')
  };

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.getData();
  }

  getData(): void {
    this.dataService.getData().subscribe(this.myObserver);
  }
}
