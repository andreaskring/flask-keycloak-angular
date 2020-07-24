import { Component } from '@angular/core';
import { DataService } from './services/data.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {

  objs : object[] = [
    {abc: 'xyz'}
  ];

  names: string[] = ["Bruce Lee", "Bob Sacremento"];

  title = 'angular';

  constructor(private dataService: DataService) {}

  getData(): Observable<Object> {
    return this.dataService.getData().subscribe(
      
    );
  }
}
