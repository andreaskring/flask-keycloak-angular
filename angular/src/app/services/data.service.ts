import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class DataService {

  constructor() { }

  getData(): object[] {
    return [{abc: "lajddlaksd"}];
  }
}
