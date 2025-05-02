/**
 * This class represents a person in the Monarchy. Each person has a name, a boolean indicating if they are alive, and a list of children.
 */
class Person {
  constructor(name) {
    this.name = name;
    this.isAlive = true;
    this.children = [];
  }
}

/**
 * This class represents a Monarchy. It has a king, and a list of persons in the Monarchy. The Monarchy class has the following methods:
 * - birth(childName, parentName): A new person with the name childName is born to parentName. The new person is alive.
 * - death(name): The person with the name name is dead.
 * - getOrderOfSuccession(): Returns a list containing the names of the persons in the order of succession
 */
class Monarchy {
  constructor(king) {
    this.king = new Person(king);
    this._persons = {
      [this.king.name]: this.king
    };
  }

  /**
   * This function creates a new person with the name childName and adds it to the list of children of the person with the
   * name parentName.
   * Our solution's time complexity is O(1) because we can directly access the person by name.
   * Our solution's space complexity is O(1) because we are not using any additional space.
   * @param {string} childName
   * @param {string} parentName
   * @returns {void}
   */
  birth(childName, parentName) {
    const parents = this._persons[parentName];
    const newChild = new Person(childName);
    parents.children.push(newChild);
    this._persons[childName] = newChild;
  }

  /**
   * This function sets the isAlive property of the person with the name name to false.
   * Our solution's time complexity is O(1) because we can directly access the person by name.
   * Our solution's space complexity is O(1) because we are not using any additional space.
   * @param {string} name
   * @returns {void}
   */
  death(name) {
    const person = this._persons[name];
    if (person === undefined) {
      return null;
    }
    person.isAlive = false;
  }

  /**
   * This function returns a list containing the names of the persons in the order of succession.
   * Our solution's time complexity is O(n) where n is the number of persons in the Monarchy. This is because we need to traverse the list of persons.
   * Our solution's space complexity is O(n) where n is the number of persons in the Monarchy. This is because we store the order of succession in a list.
   * @returns {string[]}
   */
  getOrderOfSuccession() {
    const order = [];
    this._dfs(this.king, order);
    return order;
  }

  /**
   * This function performs a depth-first traversal of the Monarchy starting from the current person and adds the names of the persons in the order of succession to the list order.
   * Our solution's time complexity is O(n) where n is the number of persons in the Monarchy. This is because we need to traverse the list of persons.
   * Our solution's space complexity is O(n) where n is the number of persons in the Monarchy. This is because we store the order of succession in a list.
   * @param {Person } current
   * @param {string[]} order
   * @returns {void}
   */
  _dfs(currentPerson, order) {
    if (currentPerson.isAlive) {
      order.push(currentPerson.name);
    }
    for (let i = 0; i < currentPerson.children.length; i++) {
      this._dfs(currentPerson.children[i], order);
    }
  }
}

const monarchy = new Monarchy('Jake');
console.log(monarchy)
monarchy.birth("Catherine", "Jake");
console.log(monarchy)
monarchy.birth('Tom', 'Jake');
console.log(monarchy)
monarchy.birth("Celine", "Jake");
console.log(monarchy)
monarchy.birth("Jane", "Catherine");
console.log(monarchy)
monarchy.birth("Peter", "Celine");
console.log(monarchy)
monarchy.birth("Farah", "Jane");
console.log(monarchy)
monarchy.birth("Mark", "Catherine");
console.log(monarchy)
console.log(monarchy.getOrderOfSuccession());
monarchy.death("Jake");
console.log(monarchy)
monarchy.death("Jane");
console.log(monarchy)
console.log(monarchy.getOrderOfSuccession());